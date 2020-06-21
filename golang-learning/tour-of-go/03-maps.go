/* Exercise: Maps */

package main

import (
	"fmt"
	"strings"

	"golang.org/x/tour/wc"
)

// WordCount : my word count
func WordCount(s string) map[string]int {
	fmt.Println("Fields are %q", strings.Fields(s))
	var count = make(map[string]int)

	for _, c := range strings.Fields(s) {
		//fmt.Println(i, c, count[c])
		count[c] += 1
	}
	fmt.Println(count)

	return count
}

func main() {
	wc.Test(WordCount)
}
