package main

import (
	"context"
	"fmt"
	"log"
	"net/http"
	"os"

	"github.com/joho/godotenv"
	"github.com/tmc/langchaingo/llms"
	"github.com/tmc/langchaingo/llms/ollama"
)

var prompt = `Explain step by step, explicitly stating each assumption and inference: What are the long-term economic effects of quantum computing on cryptography?`

func main() {
	err := godotenv.Load()
	if err != nil {
		log.Fatal("Error loading .env file")
	}

	HOST := os.Getenv("OLLAMA_URL")

	llm, err := ollama.New(ollama.WithModel("deepseek-r1:14b"), ollama.WithServerURL(HOST), ollama.WithHTTPClient(&http.Client{}))

	if err != nil {
		log.Fatal(err)
	}

	ctx := context.Background()

	completion, err := llms.GenerateFromSinglePrompt(ctx, llm, prompt,
		llms.WithStreamThinking(true),
		llms.WithStreamingFunc(func(ctx context.Context, chunk []byte) error {
			fmt.Print(string(chunk))
			return nil
		}),
	)

	if err != nil {
		log.Fatal(err)
	}

	_ = completion
}
