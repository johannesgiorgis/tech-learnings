/* Exercise: Slices

Possible functions:
- (x + y)/2
- x * y
- x ^ y
*/

package main

import (
	"fmt"

	"golang.org/x/tour/pic"
)

// Pic : picture function
func Pic(dx, dy int) [][]uint8 {
	fmt.Println(dx, dy)

	p := make([][]uint8, dy)
	for i := range p {
		p[i] = make([]uint8, dx)
	}

	for y, row := range p {
		for x := range row {
			row[x] = uint8(x * y)
		}
	}

	return p
}

func main() {
	pic.Show(Pic)
}
