package main

import "math"

func main() {
	var limit uint = 1000
	var zahl, zaehler uint
	var primzahl bool

	for zahl = 2; zahl <= limit; zahl++ {

		primzahl = true

		for zaehler = 2; zaehler <= zahl/2; zaehler++ {
			if math.Mod(float64(zahl), float64(zaehler)) == 0 {
				primzahl = false
				break
			}
		}

		if primzahl == true {
			println(zahl, " is prime")
		}
	}

}
