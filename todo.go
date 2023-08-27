package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	todos := []string{}

	for {
		fmt.Println("\nTodo List:")
		for i, todo := range todos {
			fmt.Printf("%d. %s\n", i+1, todo)
		}

		fmt.Print("\n1. Add Todo\n2. Remove Todo\n3. Exit\n\nSelect an option: ")

		var choice int
		_, err := fmt.Scanf("%d\n", &choice)
		if err != nil {
			fmt.Println("Invalid input. Please enter a number.")
			continue
		}

		switch choice {
		case 1:
			fmt.Print("Enter todo: ")
			scanner := bufio.NewScanner(os.Stdin)
			if scanner.Scan() {
				todo := scanner.Text()
				todos = append(todos, todo)
				fmt.Printf("Added: %s\n", todo)
			}
		case 2:
			fmt.Print("Enter index of todo to remove: ")
			var index int
			_, err := fmt.Scanf("%d\n", &index)
			if err != nil || index < 1 || index > len(todos) {
				fmt.Println("Invalid index.")
				continue
			}
			removedTodo := todos[index-1]
			todos = append(todos[:index-1], todos[index:]...)
			fmt.Printf("Removed: %s\n", removedTodo)
		case 3:
			fmt.Println("Exiting...")
			return
		default:
			fmt.Println("Invalid choice. Please select a valid option.")
		}
	}
}
