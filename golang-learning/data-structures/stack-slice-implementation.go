/* Stack - Slice Implementation
- https://golangbyexample.com/stack-in-golang/
*/

package main

import (
	"fmt"
	"sync"
)

type customStack1 struct {
	stack []string
	lock  sync.RWMutex
}

func (c *customStack1) Push(value string) {
	c.lock.Lock()
	defer c.lock.Unlock()
	c.stack = append(c.stack, value)
}

func (c *customStack1) Pop() error {
	len := len(c.stack)
	if len > 0 {
		c.lock.Lock()
		defer c.lock.Unlock()
		c.stack = c.stack[:len-1]
		return nil
	}
	return fmt.Errorf("Pop Error: Stack is empty")
}

func (c *customStack1) Front() (string, error) {
	len := len(c.stack)
	if len > 0 {
		c.lock.Lock()
		defer c.lock.Unlock()
		return c.stack[len-1], nil
	}
	return "", fmt.Errorf("Peep Error: Stack is empty")
}

func (c *customStack1) Size() int {
	return len(c.stack)
}

func (c *customStack1) Empty() bool {
	return len(c.stack) == 0
}

// my own addition
func newStack() *customStack1 {
	return &customStack1{
		stack: make([]string, 0),
	}
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
