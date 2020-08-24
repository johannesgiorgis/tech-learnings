/* Queue - List Implementation
- https://golangbyexample.com/queue-in-golang/
*/

package main

import (
	"fmt"
	"sync"
)

type customQueue1 struct {
	queue []string
	lock  sync.RWMutex
}

func (c *customQueue1) Enqueue(value string) {
	c.lock.Lock()
	defer c.lock.Unlock()
	c.queue = append(c.queue, value)
}

func (c *customQueue1) Dequeue() error {
	if len(c.queue) > 0 {
		c.lock.Lock()
		defer c.lock.Unlock()
		c.queue = c.queue[1:]
		return nil
	}
	return fmt.Errorf("Dequeue Error: Queue is empty")
}

func (c *customQueue1) Front() (string, error) {
	if len(c.queue) > 0 {
		c.lock.Lock()
		defer c.lock.Unlock()
		return c.queue[0], nil
	}
	return "", fmt.Errorf("Peep Error: Queue is empty")
}

func (c *customQueue1) Size() int {
	return len(c.queue)
}

func (c *customQueue1) Empty() bool {
	return len(c.queue) == 0
}

// my own addition
func newQueue() *customQueue1 {
	return &customQueue1{
		queue: make([]string, 0),
	}
}

func main() {
	myQueue := newQueue()

	fmt.Printf("Enqueue: A\n")
	myQueue.Enqueue("A")
	fmt.Printf("Enqueue: B\n")
	myQueue.Enqueue("B")
	fmt.Printf("Size: %d\n", myQueue.Size())
	for myQueue.Size() > 0 {
		frontVal, _ := myQueue.Front()
		fmt.Printf("Front: %s\n", frontVal)
		fmt.Printf("Dequeue: %s\n", frontVal)
		myQueue.Dequeue()
	}
	fmt.Printf("Size: %d\n", myQueue.Size())
}
