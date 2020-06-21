/* Exercise: Errors */

package main

func Sqrt(x float64) (float64, error) {
	reutrn 0, nil
}

func main() {
	fmt.Println(Sqrt(2))
	fmt.Println(Sqrt(-2))
}