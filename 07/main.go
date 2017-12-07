package main

import (
	"os"
	"bufio"
	"strings"
	"strconv"
	"fmt"
)

var (
	programMap = map[string]*Program{}
	nameForSearch string
)

type Program struct {
	Name string
	Value int
	Weight int
	Parent string
	Children []string
	ParentRef *Program
	ChildRefs []*Program
}

func getInt(s string) int {
	left := strings.Index(s, "(")
	right := strings.Index(s, ")")
	integer, _ := strconv.Atoi(s[left+1 : right])
	return integer
}

func setWeight(program *Program) int {
	weight := program.Value
	for _, child := range program.ChildRefs {
		weight += setWeight(child)
	}
	program.Weight = weight
	return program.Weight
}

func main() {
	file, _ := os.Open("input1.txt")
	defer file.Close()

	// Set up map of programs

	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		if strings.Contains(scanner.Text(), "->") {
			fields := strings.Fields(scanner.Text())
			childStrings := fields[3:]
			for i, _ := range childStrings {
				childStrings[i] = strings.Replace(childStrings[i], ",", "", -1)
			}
			program := &Program{
				Name: fields[0],
				Value: getInt(fields[1]),
				Children: childStrings,
			}
			programMap[program.Name] = program
			nameForSearch = program.Name

		} else {
			fields := strings.Fields(scanner.Text())
			program := &Program{
				Name: fields[0],
				Value: getInt(fields[1]),
			}
			programMap[program.Name] = program
			nameForSearch = program.Name
		}
	}

	// Convert soft references to real pointers now that we've initialized our programs
	for name, program := range programMap {
		for _, child := range program.Children {
			program.ChildRefs = append(program.ChildRefs, programMap[child])
			programMap[child].ParentRef = programMap[name]
		}
	}

	// Find root of tree, identify
	root := programMap[nameForSearch].ParentRef
	for root.ParentRef != nil {
		root = root.ParentRef
	}
	fmt.Printf("Tree root is %s\n", root.Name)

	// Set weights
	setWeight(root)
	fmt.Println(root.Weight)

	// Identify programs with unbalanced children
	for _, program := range programMap {
		weight := 0
		for _, child := range program.ChildRefs {
			if weight == 0 {
				weight = child.Weight
			} else {
				if child.Weight != weight {
					fmt.Printf("Child weight %d does not match existing %d\n", child.Weight, weight)
					fmt.Printf("Found unbalanced children for program %s:\n", program.Name)
					for _, unbalanced := range program.ChildRefs {
						fmt.Printf("Child named %s with weight %d and value %d causing imbalance\n",
							unbalanced.Name, unbalanced.Weight, unbalanced.Value)
					}
					break
				}
			}
		}
	}
}