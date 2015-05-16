#MIPS Reference

| Name | Command | Binary | Definition |
|:------:|---------|--------|------------|
| **Word**	| .word i	| `iiii iiii iiii iiii iiii iiii iiii iiii` |
| **Add** | add $d $s $t | `0000 00ss ssst tttt dddd d000 0010 0000` | $d = $s + $t |
| **Subtract** | sub $d $s $t | `0000 00ss ssst tttt dddd d000 0010 0010` | $d = $s - $t |
| **Multiply** | mult $s $t | `0000 00ss ssst tttt 0000 0000 0001 1000` | hi:lo = $s * $t |
| **Multiply Unsigned** | multu $s $t | `0000 00ss ssst tttt 0000 0000 0001 1001` | hi:lo = $s * $t |
| **Divide** | div $s $t | `0000 00ss ssst tttt 0000 0000 0001 1010` | lo = $s / $t; hi = $s % $t |
| **Divide Unsigned** | divu $s $t | `0000 00ss ssst tttt 0000 0000 0001 1011` | lo = $s / $t; hi = $s % $t |
| **Move From High** | mfhi $d | `0000 0000 0000 0000 dddd d000 0001 0000` | $d = hi|
| **Move from Lo** | mflo $d | `0000 0000 0000 0000 dddd d000 0001 0010` | $d = lo |
| **Load Immediate And Skip** | lis $d | `0000 0000 0000 0000 dddd d000 0001 0100 `| $d = MEM[pc]; pc = pc + 4 |
| **Load Word** | lw $t i($s) | `1000 11ss ssst tttt iiii iiii iiii iiii` | $t = MEM[$s + i] |
| **Store Word** | sw $t i($s) | `1010 11ss ssst tttt iiii iiii iiii iiii` | MEM[$s + i] = $t |
| **Set Less Than** | slt $d $s $t | `0000 00ss ssst tttt dddd d000 0010 1010` | $d = 1 if $s < $t; 0 o/w |
| **Set Less Than Unsigned** | sltu $d $s $t | `0000 00ss ssst tttt dddd d000 0010 1011` | $d = 1 if $s < $t; 0 o/w |
| **Branch On Equal** | beq $s $t i | `0001 00ss ssst tttt iiii iiii iiii iiii` | if ($s == $t) pc += i * 4 |
| **Branch On Not Equal** | bne $s $t i | `0001 01ss ssst tttt iiii iiii iiii iiii` | if ($s != $t) pc += i * 4 |
| **Jump Register** | jr $s | `0000 00ss sss0 0000 0000 0000 0000 1000` | pc = $s|
| **Jump Register and Link** | jalr $s | `0000 00ss sss0 0000 0000 0000 0000 1001` | temp = $s; $31 = pc; pc = temp |