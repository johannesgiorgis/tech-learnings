package main

import (
	"fmt"
	"log"
	"net/http"
)

func main() {
	fmt.Println("Starting web server on port 8080...")
	http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
		w.Write([]byte(`
			<html>
				<head>
					<title>Chat</title>
				</head>
				<body>
				Let's chat!
				</body>
			</html>
		`))
	})
	// start the web server
	if err := http.ListenAndServe(":8080", nil); err != nil {
		log.Fatal("ListenAndServe:", err)
	}
}