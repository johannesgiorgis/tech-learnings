package main

import (
	"fmt"
	"math"
)

// Sqrt : Custom Square Root
func Sqrt(x float64) float64 {
	z := x / 2
	i := 0
	newZ := float64(0)
	for i < 10 {
		newZ -= (z*z - x) / (2 * z)
		println(z, newZ-z)
		z = newZ
		i++
	}
	return z
}

func main() {
	fmt.Println(Sqrt(2))
	fmt.Println(math.Sqrt(2))
}
