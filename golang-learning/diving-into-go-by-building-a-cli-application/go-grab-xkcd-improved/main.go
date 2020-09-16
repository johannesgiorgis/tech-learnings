package main

import (
	"go-grab-xkcd-improved/grabxkcd"
	"os"
)

func main() {
	os.Exit(grabxkcd.CLI(os.Args[1:]))
}
