set handle [open day1.in r]
set input [read -nonewline $handle]
close $handle

while {[regsub -all {\((\.*)\)} $input {.\1.} input] > 0} {}
puts [expr {[regexp -all {\(} $input] - [regexp -all {\)} $input]}]
puts [expr {[string first ) $input] + 1}]
