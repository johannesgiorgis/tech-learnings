/* Queue - List Implementation
- https://golangbyexample.com/queue-in-golang/
*/

package main

import (
	"container/list"
	"fmt"
)

type customQueue struct {
	queue *list.List
}

func (c *customQueue) Enqueue(value string) {
	c.queue.PushBack(value)
}

func (c *customQueue) Dequeue() error {
	if c.queue.Len() > 0 {
		elem := c.queue.Front()
		c.queue.Remove(elem)
	}
	return fmt.Errorf("Dequeue Error: Queue is empty")
}

func (c *customQueue) Front() (string, error) {
	if c.queue.Len() > 0 {
		if val, ok := c.queue.Front().Value.(string); ok {
			return val, nil
		}
		return "", fmt.Errorf("Peep Error: Queue Datatype is incorrect")
	}
	return "", fmt.Errorf("Peep Error: Queue is empty")
}

func (c *customQueue) Size() int {
	return c.queue.Len()
}

func (c *customQueue) Empty() bool {
	return c.queue.Len() == 0
}

// my own addition
func newQueue() *customQueue {
	return &customQueue{
		queue: list.New(),
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
