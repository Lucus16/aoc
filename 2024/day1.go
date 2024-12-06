package main

import "slices"
import "fmt"
import "os"
import "io"

func day1(path string) (answer1, answer2 int, err error) {
	file, err := os.Open(path)
	if err != nil {
		return
	}
	defer file.Close()
	var as, bs []int
	for {
		var a, b int
		_, err = fmt.Fscanln(file, &a, &b);
		if err == io.EOF {
			err = nil
			break
		}
		if err != nil {
			return
		}
		as = append(as, a)
		bs = append(bs, b)
	}
	slices.Sort(as)
	slices.Sort(bs)
	for i := range as {
		if as[i] < bs[i] {
			answer1 += bs[i] - as[i]
		} else {
			answer1 += as[i] - bs[i]
		}
	}
	bcounts := make(map[int]int)
	for _, b := range bs {
		c, _ := bcounts[b]
		bcounts[b] = c + 1
	}
	for _, a := range as {
		c, _ := bcounts[a]
		answer2 += a * c
	}
	return
}
