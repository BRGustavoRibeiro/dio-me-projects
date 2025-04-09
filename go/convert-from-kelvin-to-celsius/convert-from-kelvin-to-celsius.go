package main

import "fmt"

func main() {
	fmt.Println("Temperature Conversion (K -> C)")
	fmt.Printf("Insert the value in Kelvin: ")

	var kelvinVal float64
	if _, err := fmt.Scan(&kelvinVal); err != nil {
		fmt.Printf("You inserted an invalid number: %s\n", err)
		return
	}

	celsiusVal := kelvinVal - 273

	fmt.Println(kelvinVal, "K is", celsiusVal, "Cº")
}
