package main

import (
	"fmt"
	"sort"
)

func main() {
	list := [][]int{{1, 4}, {3, 8}, {4, 7}, {5, 8}}
	ans := 0
	count := 0
	data := [][]int{}

	for _, item := range list {
		data = append(data, []int{item[0], 0})
		data = append(data, []int{item[1], 1})
	}

	sort.SliceStable(data, func(i, j int) bool {
		return data[i][0] < data[j][0]
	})

	for _, item := range data {
		if item[1] == 0 {
			count++
		}

		if item[1] == 1 {
			count--
		}

		if ans < count {
			ans = count
		}
	}
	fmt.Println(ans)
}
