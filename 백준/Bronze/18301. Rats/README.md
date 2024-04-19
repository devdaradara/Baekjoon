# [Bronze V] Rats - 18301 

[문제 링크](https://www.acmicpc.net/problem/18301) 

### 성능 요약

메모리: 31120 KB, 시간: 40 ms

### 분류

사칙연산, 수학

### 제출 일자

2024년 4월 19일 10:21:58

### 문제 설명

<p style="user-select: auto !important;">To celebrate the Lunar New Year of the Rat, Douglas decides to count the number of rats living in his area. It is impossible for him to find all rats, as they tend to be well hidden. However, on the first day of the new year, Douglas manages to capture n<sub style="user-select: auto !important;">1</sub> rats, and marks each of them with an ear tag before releasing them. On the second day of the new year, Douglas captures n<sub style="user-select: auto !important;">2</sub> rats, and observes that n<sub style="user-select: auto !important;">12</sub> of them had been marked during the first day.</p>

<p style="user-select: auto !important;">Douglas is asking for your help to estimate the total number of rats in his area. Looking up in your statistics textbook, you propose using the Chapman estimator N, given by:</p>

<p style="text-align: center; user-select: auto !important;">N := ⌊(n<sub style="user-select: auto !important;">1</sub> + 1)(n<sub style="user-select: auto !important;">2</sub> + 1)/(n<sub style="user-select: auto !important;">12</sub> + 1) - 1⌋</p>

<p style="user-select: auto !important;">where ⌊x⌋ is the floor of a real number x, i.e., the closest integer less than or equal to x.</p>

### 입력 

 <p style="user-select: auto !important;">The input consists of a single line, with three space-separated integers: n<sub style="user-select: auto !important;">1</sub>, n<sub style="user-select: auto !important;">2</sub>, n<sub style="user-select: auto !important;">12</sub>, in that order.</p>

### 출력 

 <p style="user-select: auto !important;">The output should contain a single line with the single integer N.</p>

