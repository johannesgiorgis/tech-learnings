package main

import (
	"flag"
	"fmt"
	"go-grab-xkcd/client"
	"log"
	"time"
)

func main() {
	// Read command arguments
	comicNo := flag.Int(
		"n", int(client.LatestComic), "Comic number to fetch (default latest)",
	)
	clientTimeout := flag.Int64(
		"t", int64(client.DefaultClientTimeout.Seconds()), "Client timeout in seconds",
	)
	saveImage := flag.Bool(
		"s", false, "Save image to current directory",
	)
	outputType := flag.String(
		"o", "text", "Print output in format: text/json",
	)
	flag.Parse()

	// Instantiate the XKCDClient
	XKCDClient := client.NewXKCDClient()
	XKCDClient.SetTimeout(time.Duration(*clientTimeout) * time.Second)

	// Fetch from API using the XKCDClient
	comic, err := XKCDClient.Fetch(client.ComicNumber(*comicNo), *saveImage)
	if err != nil {
		log.Println(err)
	}

	// Output
	if *outputType == "json" {
		fmt.Println(comic.JSON())
	} else {
		fmt.Println(comic.PrettyString())
	}
}
