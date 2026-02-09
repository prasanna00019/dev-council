from app.agents.project_lead import get_project_lead_agent
from app.agents.milestone import get_milestone_agent
from langchain_core.messages import HumanMessage
from app.tools.save_file import save_file, markdown_to_pdf


class ManagerAgent:
    def __init__(self):
        self.project_lead = get_project_lead_agent()
        self.milestone_agent = get_milestone_agent()

    def process_request(self, user_query: str):
        print(f"--- Manager: Received request: {user_query} ---")
        print("--- Manager: Delegating to Project Lead ---")
        project_lead_response = self.project_lead.invoke(
            {"messages": [HumanMessage(content=user_query)]}
        )

        project_lead_content = project_lead_response
        if isinstance(project_lead_response, dict) and "messages" in project_lead_response:
            messages = project_lead_response["messages"]
            if messages:
                project_lead_content = messages[-1].content if hasattr(messages[-1], "content") else str(messages[-1])
        
        save_file("project_plan.md", project_lead_content)

        print("--- Manager: Received Project Plan ---")
        print(project_lead_response)
        
        # Convert markdown to PDF
        print("--- Manager: Converting Project Plan to PDF ---")
        markdown_to_pdf("project_plan.md", "project_plan.pdf")
        print("--- Manager: Project Plan PDF generated ---")
        
 
        print("--- Manager: Delegating to Milestone Agent ---")
        milestone_response = self.milestone_agent.invoke(
            {
                "messages": [
                    HumanMessage(
                        content=f"Create a milestone table based on this plan:\n\n{project_lead_content}"
                    )
                ]
            }
        )
        
        
        milestone_content = milestone_response
        if isinstance(milestone_response, dict) and "messages" in milestone_response:
           
            messages = milestone_response["messages"]
            if messages:
                milestone_content = messages[-1].content if hasattr(messages[-1], "content") else str(messages[-1])
        
        print("--- Manager: Received Milestone Table ---")
        print(milestone_content)
        save_file("milestone.md", milestone_content)
        
        # Convert milestone markdown to PDF
        print("--- Manager: Converting Milestone Table to PDF ---")
        markdown_to_pdf("milestone.md", "milestone.pdf")
        print("--- Manager: Milestone Table PDF generated ---")
        return


def get_manager():
    return ManagerAgent()
