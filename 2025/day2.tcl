set handle [open day2.in r]
set input [split [read -nonewline $handle] ,]
close $handle

source math.tcl

proc concatmap args { concat {*}[uplevel 1 [list lmap {*}$args]] }

foreach max_repeats [list 2 10] {
        puts [sum [lsort -integer -unique [concatmap range $input {
                lassign [split $range -] start end
                concatmap repeats [range 2 [expr {$max_repeats + 1}]] {
                        if {[string bytelength $start] % $repeats == 0} then {
                                set start1 [string byterange $start 0 [expr {[string bytelength $start] / $repeats - 1}]]
                                if {[string repeat $start1 $repeats] < $start} then {incr start1}
                        } else {
                                set start1 [expr {pow(10, [string bytelength $start] / $repeats)}]
                        }
                        if {[string bytelength $end] % $repeats == 0} then {
                                set end1 [string byterange $end 0 [expr {[string bytelength $end] / $repeats - 1}]]
                                if {[string repeat $end1 $repeats] > $end} then {incr end1 -1}
                        } else {
                                set end1 [expr {pow(10, [string bytelength $end] / $repeats) - 1}]
                        }
                        incr end1
                        if {$start1 < $end1} {
                                concatmap part [range $start1 $end1] {
                                        string repeat $part $repeats
                                }
                        }
                }
        }]]]
}
