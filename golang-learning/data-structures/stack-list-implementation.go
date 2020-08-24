/* Stack - List Implementation
- https://golangbyexample.com/stack-in-golang/
*/

package main

import (
	"container/list"
	"fmt"
)

type customStack struct {
	stack *list.List
}

func (c *customStack) Push(value string) {
	c.stack.PushFront(value)
}

func (c *customStack) Pop() error {
	if c.stack.Len() > 0 {
		elem := c.stack.Front()
		c.stack.Remove(elem)
	}
	return fmt.Errorf("Pop Error: Stack is empty")
}

func (c *customStack) Front() (string, error) {
	if c.stack.Len() > 0 {
		if val, ok := c.stack.Front().Value.(string); ok {
			return val, nil
		}
		return "", fmt.Errorf("Peep Error: Stack Datatype is incorrect")
	}
	return "", fmt.Errorf("Peep Error: Stack is empty")
}

func (c *customStack) Size() int {
	return c.stack.Len()
}

func (c *customStack) Empty() bool {
	return c.stack.Len() == 0
}

// my own addition
func newStack() *customStack{
	stack: list.New(),
}

func main() {
	myStack := newStack()

	fmt.Printf("Push: A\n")
	myStack.Push("A")
	fmt.Printf("Push: B\n")
	myStack.Push("B")
	fmt.Printf("Size: %d\n", myStack.Size())
	for myStack.Size() > 0 {
		frontVal, _ := myStack.Front()
		fmt.Printf("Front: %s\n", frontVal)
		fmt.Printf("Pop: %s\n", frontVal)
		myStack.Pop()
	}
	fmt.Printf("Size: %d\n", myStack.Size())
}
