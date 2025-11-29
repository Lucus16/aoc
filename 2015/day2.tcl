set handle [open day2.in r]
set lines [split [read -nonewline $handle] "\n"]
close $handle

source math.tcl

puts [sum [lmap line $lines {
        scan $line "%dx%dx%d" l w h
        set sides [list [expr {$l * $w}] [expr {$w * $h}] [expr {$h * $l}]]
        expr {2 * [sum $sides] + [min $sides]}
}]]

puts [sum [lmap line $lines {
        lassign [lsort -integer [split $line x]] l w h
        expr {2 * $l + 2 * $w + $l * $w * $h}
}]]
