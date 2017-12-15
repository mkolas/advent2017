package main

import "fmt"

type GenConfig struct {
	Value int
	Factor int
}

type PickyConfig struct {
	GenConfig
	Multiple int
}

func adventGenerator(state *GenConfig) int {
	state.Value = (state.Value*state.Factor)%2147483647
	return state.Value
}

func pickyGenerator(state *PickyConfig) int {
	for {
		state.GenConfig.Value = (state.GenConfig.Value*state.GenConfig.Factor)%2147483647
		if state.GenConfig.Value % state.Multiple == 0 {
			return state.GenConfig.Value
		}
	}

}

func main(){

	// part 1
	aState := &GenConfig{
		Value: 277,
		Factor: 16807,
	}

	bState := &GenConfig{
		Value:349,
		Factor: 48271,
	}

	loop := 0
	count := 0
	for loop <= 40000000 {
		if adventGenerator(aState) & 65535 == adventGenerator(bState) & 65535{
			count++
		}
		loop++
	}

	fmt.Printf("judge's count: %d\n", count)

	// part 2
	cState := &PickyConfig{
		Multiple: 4,
		GenConfig: GenConfig{
			Value: 277,
			Factor: 16807,
		},
	}

	dState := &PickyConfig{
		Multiple: 8,
		GenConfig: GenConfig{
			Value: 349,
			Factor: 48271,
		},
	}

	loop = 0
	count = 0
	for loop <= 5000000 {
		if pickyGenerator(cState) & 65535 == pickyGenerator(dState) & 65535{
			count++
		}
		loop++
	}

	fmt.Printf("picky judge's count: %d\n", count)
}
