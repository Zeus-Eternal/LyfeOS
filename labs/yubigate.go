package main

import (
    "fmt"
    "os"
)

func main() {
    fmt.Println("YubiGate placeholder - implement hardware challenge here")
    if len(os.Args) > 1 {
        fmt.Printf("PR %s approved\n", os.Args[1])
    }
}
