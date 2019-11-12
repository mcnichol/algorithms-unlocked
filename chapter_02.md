# Algorithms Unlocked - Ch 2

## Procedures

### Linear Search
#### Inputs:
* A: an array
* n: the number of elements in A to search through
* x: the value being searched for

#### Output: 
Either an index **i**  for which **A\[i\] = x**, or the special value `NOT-FOUND`, which could be any invalid index into the array, such as 0 or any negative integer.

#### Operations:
1. Set *answer* to `NOT-FOUND`
2. For each index *i*, going from *1* &rarr; *n*, in order:  
   a. If **A\[i] = x** then set *answer* to the value of i  
3. Return the value of *answer* as the output

#### Operation Breakdown:
<table>
<thead><tr><td>Op #</td><td>Op Count</td><td>Desc</td><td>Notation</td></tr></thead>
<tbody> 
<tr style="text-align: right; color: #000;"><td>1</td><td>1</td><td></td><td style="color: red">t<sub>1</sub></td></tr>
<tr style="text-align: right"><td>2</td><td>n+1</td><td>Test i &lt; n for loop</td><td style="color: blue">t&prime;<sub>2</sub></td></tr>
<tr style="text-align: right"><td>2</td><td>n</td><td>i++</td><td style="color: green">t&Prime;<sub>2</sub></td></tr>
<tr style="text-align: right"><td>2a</td><td>n</td><td>Test A[i] = x</td><td style="color: orange">t&prime;<sub>2A</sub></td></tr>
<tr style="text-align: right"><td>2a</td><td>n</td><td>When A[i] = x <b><sup>1</sup></b></td><td style="color: #AC31DD">t&Prime;<sub>2A</sub></td></tr>
<tr style="text-align: right"><td>3</td><td>1</td><td></td><td style="color: #DD32CE">t<sub>3</sub></td></tr>
</tbody>
</table>

**Table Notes:**  
**<sup>1</sup>** There is no restriction on the correct value existing within **A\[n]** multiple times. An op count of n reflects the upper bound of the value existing at every index. 

##### Total Operation Counts (Bounds):
*Lower:*&nbsp;&nbsp;&nbsp;&nbsp; <span style="color: red">t<sub>1</sub></span> + <span style="color: blue">(t&prime;<sub>2</sub> * (n + 1))</span> + <span style="color: green">(t&Prime;<sub>2</sub> * n)</span> + <span style="color: orange">(t&prime;<sub>2A</sub> * n)</span> + <span style="color: #AC31DD">(t&Prime;<sub>2A</sub> * 0)</span> + <span style="color:#DD32CE">t3</span>  
*Upper:*&nbsp;&nbsp;&nbsp;&nbsp; <span style="color: red">t<sub>1</sub></span> + <span style="color: blue">(t&prime;<sub>2</sub> * (n + 1))</span> + <span style="color: green">(t&Prime;<sub>2</sub> * n)</span> + <span style="color: orange">(t&prime;<sub>2A</sub> * n)</span> + <span style="color: #AC31DD">(t&Prime;<sub>2A</sub> * n)</span> + <span style="color:#DD32CE">t3</span>  


**Simplified:**  
*Lower:* &nbsp;&nbsp;&nbsp;&nbsp; <span style="color: red">t<sub>1</sub></span> + <span style="color: blue">t&prime;<sub>2</sub></span> + <span style="color:#DD32CE">t3</span> + n(<span style="color: blue">t&prime;<sub>2</sub></span> + <span style="color: green">t&Prime;<sub>2</sub></span> + <span style="color: orange">t&prime;<sub>2A</sub></span>)  
*Upper:* &nbsp;&nbsp;&nbsp;&nbsp; <span style="color: red">t<sub>1</sub></span> + <span style="color: blue">t&prime;<sub>2</sub></span> + <span style="color:#DD32CE">t3</span> + n(<span style="color: blue">t&prime;<sub>2</sub></span> + <span style="color: green">t&Prime;<sub>2</sub></span> + <span style="color: orange">t&prime;<sub>2A</sub></span> + <span style="color: #AC31DD">t&Prime;<sub>2A</sub></span>)


### Better Linear Search
#### Inputs:
* A: an array
* n: the number of elements in A to search through
* x: the value being searched for

#### Output: 
Either an index **i**  for which **A\[i\] = x**, or the special value `NOT-FOUND`, which could be any invalid index into the array, such as 0 or any negative integer.

#### Operations:
1. For i = 1 to n:For each index *i*, going from *1* &rarr; *n*, in order:  
   a. If **A\[i] = x**, then return the value of i as the output
2. Return `NOT-FOUND` as the output.

### Sentinel Linear Search
#### Inputs:
* A: an array
* n: the number of elements in A to search through
* x: the value being searched for

#### Output: 
Either an index **i**  for which **A\[i\] = x**, or the special value `NOT-FOUND`, which could be any invalid index into the array, such as 0 or any negative integer.

#### Operations:
1. Save **A\[n]** into *last* and then put *x* into A\[n]
2. Set *i* to 1
3. While **A\[i] &ne; x**, do the following:
  a. Increment *i*
4. Restore **A\[n]** from *last*
5. If **i < n** or **A\[n] = x**, then return the value of *i* as the output.
6. Otherwise, return `NOT-FOUND` as the output.