/* 1.1 Is Unique? */

package main

import (
	"fmt"
	"sort"
	"strings"
)

func main() {
	fmt.Println("Is Unique?")
	words := []string{
		"carts",
		"hello",
		"man",
	}
	for _, s := range words {
		fmt.Printf("%s -> is unique? %t|%t|%t\n\n", s, isUnique(s), andyIsUnqiue(s), isUniqueSort(s))
	}
}

func isUnique(s string) bool {
	// use a map
	wordMap := make(map[rune]int)

	for _, rune := range s {
		wordMap[rune]++
	}

	fmt.Printf("map: [")
	for rune, count := range wordMap {
		fmt.Printf(" %c:%d ", rune, count)
	}
	fmt.Printf("]\n")

	for _, count := range wordMap {
		if count > 1 {
			return false
		}
	}
	return true
}

func andyIsUnqiue(s string) bool {
	myMap := make(map[rune]bool)
	for _, c := range s {
		if _, ok := myMap[c]; ok {
			return false
		} else {
			myMap[c] = true
		}

	}
	return true
}

func isUniqueSort(s string) bool {
	sortedS := sortString(s)
	println(sortedS)
	lastSeen := sortedS[0]

	for i := 1; i < len(sortedS); i++ {
		if sortedS[i] == lastSeen {
			return false
		}

		lastSeen = sortedS[i]
	}
	return true
}

func sortString(w string) string {
	s := strings.Split(w, "")
	fmt.Printf("Type: %T|%v\n", s, s)
	sort.Strings(s)
	return strings.Join(s, "")
}

/*
What about if we don't use any additional data structures?

- Either sort the string (O(n * log(n)) then compare
- Compare each character to every other character in the string
*/
