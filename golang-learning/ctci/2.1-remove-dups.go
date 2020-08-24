/* 2.1 Remove Dups

Write code to remove duplicates from an unsorted linked list.
*/

package main

import "fmt"

func main() {
	fmt.Println("Remove Dups")

	/* create unsorted linked list*/
	s := &singleList{}
	s.head = &elem{value: 3}
	newElem := createNewElem(2)
	newElem.next = s.head
	s.head = newElem
	newElem = &elem{value: 42}
	newElem.next = s.head
	s.head = newElem
	newElem = &elem{value: 3}
	newElem.next = s.head
	s.head = newElem
	newElem = &elem{value: 2}
	newElem.next = s.head
	s.head = newElem
	newElem = &elem{value: -5}
	newElem.next = s.head
	s.head = newElem
	newElem = &elem{value: 100}
	newElem.next = s.head
	s.head = newElem

	s.Traverse()

	removeDups(s)

	s.Traverse()
}

func removeDups(s *singleList) {
	var prev *elem
	dups := make(map[int]bool)

	n := s.head
	for n != nil {
		d := n.value

		if _, ok := dups[d]; ok {
			// n.Remove
			prev.next = n.next
		} else {
			dups[d] = true
			prev = n
		}

		n = n.next
	}
}

// Kept getting below error:
// ./2.1-remove-dups.go:51:6: prev declared but not used
// func removeDupsNotWorking(s *singleList) (*singleList, error) {
// 	fmt.Println("Removing Duplicates")

// 	valueMap := make(map[int]int)

// 	if s.head == nil {
// 		return s, fmt.Errorf("removeDups: List is empty")
// 	}

// 	// populate our map
// 	current := s.head
// 	var prev *elem
// 	for current != nil {

// 		if _, ok := valueMap[current.value]; ok {
// 			prev = current.next
// 		} else {
// 			valueMap[current.value]++
// 		}
// 		prev = current
// 		current = current.next
// 	}
// 	return s, nil
// }

type elem struct {
	value int
	next  *elem
}

type singleList struct {
	len  int
	head *elem
}

func initList() *singleList {
	return &singleList{}
}

func createNewElem(d int) *elem {
	e := new(elem)
	e.value = d
	return e
}

func (s *singleList) Traverse() error {
	if s.head == nil {
		return fmt.Errorf("TraverseError: List is empty")
	}
	current := s.head
	for current != nil {
		// fmt.Println(current.name)
		fmt.Printf("%d -> ", current.value)
		current = current.next
	}
	fmt.Println("nil")
	return nil
}
