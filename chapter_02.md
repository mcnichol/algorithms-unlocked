# Algorithms Unlocked - Ch 2

## Procedures

### Linear Search
#### Inputs:
* A: an array
* n: the number of elements in A to search through
* x: the value being searched for

#### Output: 
Either an index **i**  for which **A\[i\] = x**, or the special value `Not-Found`, which could be any invalid index into the array, such as 0 or any negative integer.

#### Operations:
1. Set **answer** to `Not-Found`
2. For each index **i**, going from **1** &rarr; **n**, in order:  
   a. If **A\[i] = x** then set **answer** to the value of i  
3. Return the value of **answer** as the output

#### Operation Breakdown:
<table>
<thead><tr style="text-align: center"><td>Op #</td><td>Op Count</td><td>Desc</td><td>Notation</td></tr></thead>
<tbody> 
<tr style="text-align: right; color: #000;"><td>1</td><td>1</td><td><b>answer := </b><code>Not-Found</code></td><td style="color: red">t<sub>1</sub></td></tr>
<tr style="text-align: right"><td>2</td><td>n+1</td><td>Test <b>i &lt; n</b> for loop</td><td style="color: blue">t&prime;<sub>2</sub></td></tr>
<tr style="text-align: right"><td>2</td><td>n</td><td><b>i++</b></td><td style="color: green">t&Prime;<sub>2</sub></td></tr>
<tr style="text-align: right"><td>2a</td><td>n</td><td>Test <b>A[i] = x</b></td><td style="color: orange">t&prime;<sub>2A</sub></td></tr>
<tr style="text-align: right"><td>2a</td><td>n</td><td><b><sup>1</sup></b>When <b>A[i] = x</b></td><td style="color: #AC31DD">t&Prime;<sub>2A</sub></td></tr>
<tr style="text-align: right"><td>3</td><td>1</td><td><code>Not Found</code></td><td style="color: #DD32CE">t<sub>3</sub></td></tr>
</tbody>
</table>


##### Total Operation Counts (Bounds):
*Lower:*&nbsp;&nbsp;&nbsp;&nbsp; <span style="color: red">t<sub>1</sub></span> + <span style="color: blue">(t&prime;<sub>2</sub> * (n + 1))</span> + <span style="color: green">(t&Prime;<sub>2</sub> * n)</span> + <span style="color: orange">(t&prime;<sub>2A</sub> * n)</span> + <span style="color: #AC31DD">(t&Prime;<sub>2A</sub> * 0)</span> + <span style="color:#DD32CE">t3</span>  
*Upper:*&nbsp;&nbsp;&nbsp;&nbsp; <span style="color: red">t<sub>1</sub></span> + <span style="color: blue">(t&prime;<sub>2</sub> * (n + 1))</span> + <span style="color: green">(t&Prime;<sub>2</sub> * n)</span> + <span style="color: orange">(t&prime;<sub>2A</sub> * n)</span> + <span style="color: #AC31DD">(t&Prime;<sub>2A</sub> * n)</span> + <span style="color:#DD32CE">t3</span>  


<table>
<thead><tr style="text-align: center"><td>Bound Direction</td><td>Reduced Form</td><td>Asymptotic Notation</td></tr></thead>
<tbody>
<tr style="text-align: right"><td>Lower</td><td><span style="color: red">t<sub>1</sub></span> + <span style="color: blue">t&prime;<sub>2</sub></span> + <span style="color:#DD32CE">t3</span> + n(<span style="color: blue">t&prime;<sub>2</sub></span> + <span style="color: green">t&Prime;<sub>2</sub></span> + <span style="color: orange">t&prime;<sub>2A</sub></span>)</td><td>&Omega;(n)</td></tr>
<tr style="text-align: right"><td>Upper</td><td><span style="color: red">t<sub>1</sub></span> + <span style="color: blue">t&prime;<sub>2</sub></span> + <span style="color:#DD32CE">t3</span> + n(<span style="color: blue">t&prime;<sub>2</sub></span> + <span style="color: green">t&Prime;<sub>2</sub></span> + <span style="color: orange">t&prime;<sub>2A</sub></span> + <span style="color: #AC31DD">t&Prime;<sub>2A</sub></span>)</td><td>O(n)</td></tr>
</tbody>
</table>

**<b><sup>2</sup></b> <b><sup>3</sup></b>Runtime:** &Theta;(n) 

**Notes:**  
**<sup>1</sup>** There is no restriction on the correct value existing within **A\[n]** multiple times. An op count of n reflects the upper bound of the value existing at every index.   
**<sup>2</sup>** When analyzing we drop constant terms due to large enough values of **n** dominating operations rendering constants irrelevant.   
**<sup>3</sup>** When bounds O (upper) == &Omega; (lower) we can express runtime as &Theta;

### Better Linear Search
#### Inputs:
* A: an array
* n: the number of elements in A to search through
* x: the value being searched for

#### Output: 
Either an index **i**  for which **A\[i\] = x**, or the special value `Not-Found`, which could be any invalid index into the array, such as 0 or any negative integer.

#### Operations:
1. For i = 1 to n:For each index *i*, going from *1* &rarr; *n*, in order:  
   a. If **A\[i] = x**, then return the value of i as the output
2. Return `Not-Found` as the output.

#### Operation Breakdown:
<table>
<thead><tr style="text-align: center"><td>Op #</td><td>Op Count</td><td>Desc</td><td>Notation</td></tr></thead>
<tbody> 
<tr style="text-align: right"><td>1</td><td>n+1</td><td>Test <b>i &lt; n</b> for loop</td><td style="color: red">t&prime;<sub>1</sub></td></tr>
<tr style="text-align: right"><td>1</td><td>n</td><td><b>i++</b></td><td style="color: blue">t&Prime;<sub>1</sub></td></tr>
<tr style="text-align: right"><td>1a</td><td>n</td><td>Test <b>A[i] = x</b></td><td style="color: green">t&prime;<sub>1A</sub></td></tr>
<tr style="text-align: right"><td>1a</td><td>1</td><td>When <b>A[i] = x</b></td><td style="color: orange">t&Prime;<sub>1A</sub></td></tr>
<tr style="text-align: right"><td>2</td><td>1</td><td><code>Not Found</code></td><td style="color: #AC31DD">t<sub>2</sub></td></tr>
</tbody>
</table>

##### Total Operation Counts (Bounds):
*Lower:*&nbsp;&nbsp;&nbsp;&nbsp; <span style="color: red">(t&prime;<sub>1</sub> * 1)</span> + <span style="color: blue">(t&Prime;<sub>1</sub> * 1)</span> + <span style="color: green">(t&prime;<sub>1A</sub> * 1)</span> + <span style="color: orange">t&Prime;<sub>1A</sub></span> + <span style="color: #AC31DD">(t<sub>2</sub> * 0)</span>  
*Upper:*&nbsp;&nbsp;&nbsp;&nbsp; <span style="color: red">(t&prime;<sub>1</sub> * (n + 1))</span> + <span style="color: blue">(t&Prime;<sub>1</sub> * n)</span> + <span style="color: green">(t&prime;<sub>1A</sub> * n)</span> + <span style="color: orange">(t&Prime;<sub>1A</sub> * 0)</span> + <span style="color: #AC31DD">t<sub>2</sub></span>  

<table>
<thead><tr style="text-align: center"><td>Bound Direction</td><td>Reduced Form</td><td>Asymptotic Notation</td></tr></thead>
<tbody>
<tr style="text-align: right"><td>Lower</td><td><span style="color: red">t&prime;<sub>1</sub></span> + <span style="color: blue">t&Prime;<sub>1</sub></span> + <span style="color: green">t&prime;<sub>1A</sub></span> + <span style="color: orange">t&Prime;<sub>1A</sub></span></td><td>&Omega;(1)</td></tr>
<tr style="text-align: right"><td>Upper</td><td><span style="color: red">t&prime;<sub>1</sub></span> + <span style="color: #AC31DD">t<sub>2</sub></span> + n(<span style="color: red">t&prime;<sub>1</sub></span> + <span style="color: blue">t&Prime;<sub>1</sub></span> + <span style="color: green">t&prime;<sub>1A</sub></span>)</td><td>O(n)</td></tr>
</tbody>
</table>

**Runtime:** O(n) 

### Sentinel Linear Search
#### Inputs:
* A: an array
* n: the number of elements in A to search through
* x: the value being searched for

#### Output: 
Either an index **i**  for which **A\[i\] = x**, or the special value `Not-Found`, which could be any invalid index into the array, such as 0 or any negative integer.

#### Operations:
1. Save **A\[n]** into **last** and then put **x** into **A\[n]**
2. Set *i* to 1
3. While **A\[i] &ne; x**, do the following:  
  a. Increment **i**
4. Restore **A\[n]** from **last**
5. If **i < n** or **A\[n] = x**, then return the value of **i** as the output.  
6. Otherwise, return `Not-Found` as the output.

#### Operation Breakdown:
<table>
    <thead><tr style="text-align: center"><td>Op #</td><td>Op Count</td><td>Desc</td><td>Notation</td></tr></thead>
    <tbody> 
        <tr style="text-align: right"><td>1</td><td>1</td><td>Set <b>last := A[n]</b></td><td style="color: red">t&prime;<sub>1</sub></td></tr>
        <tr style="text-align: right"><td>1</td><td>1</td><td>Set <b>A[n] := x</b></td><td style="color: blue">t&Prime;<sub>1</sub></td></tr>
        <tr style="text-align: right"><td>2</td><td>1</td><td>Set <b>i := 1</b></td><td style="color: green">t<sub>2</sub></td></tr>
        <tr style="text-align: right"><td>3</td><td>n</td><td>Test <b>A[i] = x</b></td><td style="color: orange">t<sub>3</sub></td></tr>
        <tr style="text-align: right"><td>3a</td><td>n</td><td><b>i++</b></td><td style="color: #AC31DD">t<sub>3A</sub></td></tr>
        <tr style="text-align: right"><td>4</td><td>1</td><td>Swap out sentinel value with original</td><td style="color: #DD32CE">t<sub>4</sub></td></tr>
        <tr style="text-align: right"><td>5</td><td>1</td><td>Test <b>i &lt; n</b></td><td style="color: #57cbdd">t&prime;<sub>5</sub></td></tr>
        <tr style="text-align: right"><td>5</td><td>1</td><td>Test <b>A[n] = x</b></td><td style="color: #dd5578">t&Prime;<sub>5</sub></td></tr>
        <tr style="text-align: right"><td>5a</td><td>1</td><td>When <b>A[i]=x || i < n</b>, return i</td><td style="color: #3edd9b">t<sub>5a</sub></td></tr>
        <tr style="text-align: right"><td>6</td><td>1</td><td><code>Not Found</code></td><td style="color: #ddbc77">t<sub>6</sub></td></tr>
    </tbody>
</table>

##### Total Operation Counts (Bounds):
*Lower:*&nbsp;&nbsp;&nbsp;&nbsp; <span style="color: red">t&prime;<sub>1</sub></span> + <span style="color: blue">t&Prime;<sub>1</sub></span> + <span style="color: green">t<sub>2</sub></span> + <span style="color: orange">(t<sub>3</sub> * 1)</span> + <span style="color: #AC31DD">(t<sub>3A</sub> * 1)</span> + <span style="color: #DD32CE">t<sub>4</sub></span> + <span style="color: #57cbdd">t&prime;<sub>5</sub></span> + <span style="color: #dd5578">t&Prime;<sub>5</sub></span> + <span style="color: #3edd9b">t<sub>5A</sub></span> + <span style="color: #ddbc77">(t<sub>6</sub> * 0)</span>  
*Upper:*&nbsp;&nbsp;&nbsp;&nbsp; <span style="color: red">t&prime;<sub>1</sub></span> + <span style="color: blue">t&Prime;<sub>1</sub></span> + <span style="color: green">t<sub>2</sub></span> + <span style="color: orange">(t<sub>3</sub> * n)</span> + <span style="color: #AC31DD">(t<sub>3A</sub> * n)</span> + <span style="color: #DD32CE">t<sub>4</sub></span> + <span style="color: #57cbdd">t&prime;<sub>5</sub></span> + <span style="color: #dd5578">t&Prime;<sub>5</sub></span> + <span style="color: #3edd9b">(t<sub>5A * 0</sub>)</span> + <span style="color: #ddbc77">t<sub>6</sub></span>

<table>
<thead><tr style="text-align: center"><td>Bound Direction</td><td>Reduced Form</td><td>Asymptotic Notation</td></tr></thead>
<tbody>
<tr style="text-align: right"><td>Lower</td><td><span style="color: red">t&prime;<sub>1</sub></span> + <span style="color: blue">t&Prime;<sub>1</sub></span> + <span style="color: green">t<sub>2</sub></span> + <span style="color: orange">t<sub>3</sub></span> + <span style="color: #AC31DD">t<sub>3A</sub></span> + <span style="color: #DD32CE">t<sub>4</sub></span> + <span style="color: #57cbdd">t&prime;<sub>5</sub></span> + <span style="color: #dd5578">t&Prime;<sub>5</sub></span> + <span style="color: #3edd9b">t<sub>5A</sub></span></td><td>&Omega;(1)</td></tr>
<tr style="text-align: right"><td>Upper</td><td><span style="color: red">t&prime;<sub>1</sub></span> + <span style="color: blue">t&Prime;<sub>1</sub></span> + <span style="color: green">t<sub>2</sub></span> + <span style="color: #DD32CE">t<sub>4</sub></span> + <span style="color: #57cbdd">t&prime;<sub>5</sub></span> + <span style="color: #dd5578">t&Prime;<sub>5</sub></span> + <span style="color: #ddbc77">t<sub>6</sub></span> + n(<span style="color: orange">t<sub>3</sub></span> + <span style="color: #AC31DD">t<sub>3A</sub></span>) 
</td><td>O(n)</td></tr>
</tbody>
</table>

**Runtime:** O(n)