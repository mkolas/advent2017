package main

import (
	"os"
	"bufio"
	"strings"
	"strconv"
	"fmt"
)

var (
	componentList []Component
)
type Component struct {
	PinA int
	PinB int
}

func findAndRemove(list []Component, component Component) []Component {
	var indexToRemove int
	for i, element := range list {
		if element == component {
			indexToRemove = i
			break
		}
	}
	list[len(list)-1], list[indexToRemove] = list[indexToRemove], list[len(list)-1]
	return list[:len(list)-1]
}

func buildBridge(componentList []Component, pin int, size int, maxStrength *int) {
	// get list of possible components
	var options []Component
	for _, element := range componentList {
		if element.PinA == pin || element.PinB == pin {
			options = append(options, element)
		}
	}

	if len(options) == 0 {
		if size > *maxStrength {
			*maxStrength = size
		}
		return
	}
	// for each of those, continue building
	for _, element := range options {
		newSize := size + element.PinA + element.PinB
		remainingComponents := make([]Component, len(componentList))
		copy(remainingComponents, componentList)
		remainingComponents = findAndRemove(remainingComponents, element)
		var newPin int
		if element.PinA == pin {
			newPin = element.PinB
		} else {
			newPin = element.PinA
		}
		buildBridge(remainingComponents, newPin, newSize, maxStrength)
	}
}

func buildBridgeWithDepth(componentList []Component, pin int, size int, maxStrength *int, depth int, maxLength *int) {
	// get list of possible components
	var options []Component
	for _, element := range componentList {
		if element.PinA == pin || element.PinB == pin {
			options = append(options, element)
		}
	}

	if len(options) == 0 {
		if depth > *maxLength {
			*maxLength = depth
			*maxStrength = size
		} else if depth == *maxLength {
				if size > *maxLength {
					*maxStrength = size
				}
		}

		return
	}
	// for each of those, continue building
	for _, element := range options {
		newSize := size + element.PinA + element.PinB
		remainingComponents := make([]Component, len(componentList))
		copy(remainingComponents, componentList)
		remainingComponents = findAndRemove(remainingComponents, element)
		var newPin int
		if element.PinA == pin {
			newPin = element.PinB
		} else {
			newPin = element.PinA
		}
		buildBridgeWithDepth(remainingComponents, newPin, newSize, maxStrength, depth +1, maxLength)
	}
}

func main() {
	file, _ := os.Open("input1.txt")
	defer file.Close()

	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		componentString := scanner.Text()
		pinA := strings.Split(componentString, "/")[0]
		pinB := strings.Split(componentString, "/")[1]
		pinAInt, _ := strconv.Atoi(pinA)
		pinBInt, _ := strconv.Atoi(pinB)
		component := Component{
			PinA: pinAInt,
			PinB: pinBInt,
		}
		componentList = append(componentList, component)
	}
	fmt.Println(componentList)

	startingPin := 0
	maxStrength := 0
	maxS := &maxStrength

	// part 1
	buildBridge(componentList, startingPin, 0, maxS)

	fmt.Println(maxStrength)

	// part 2

	maxStrength2 := 0
	MaxS2 := &maxStrength2
	maxLength := 0
	maxL := &maxLength

	buildBridgeWithDepth(componentList, startingPin, 0, MaxS2, 0, maxL)

	fmt.Println(maxStrength2)
	fmt.Println(maxLength)

}
