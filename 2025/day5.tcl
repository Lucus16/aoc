set handle [open day5.in r]
set input [read $handle]
close $handle

source math.tcl

proc concatmap args { concat {*}[uplevel 1 [list lmap {*}$args]] }

set events [concatmap line $input {
        lassign [split $line -] first_fresh last_fresh
        if {$last_fresh eq ""} then {
                list [list $first_fresh query]
        } else {
                list [list $first_fresh fresh] [list [expr {$last_fresh + 1}] spoiled]
        }
}]

set potentially_fresh 0
set actually_fresh 0
set in_fresh_ranges 0
foreach event [lsort -integer -index 0 $events] {
        lassign $event id type
        switch $type {
                fresh {
                        if !$in_fresh_ranges then {
                                incr potentially_fresh [expr {-$id}]
                        }
                        incr in_fresh_ranges
                }
                spoiled {
                        incr in_fresh_ranges -1
                        if !$in_fresh_ranges then {
                                incr potentially_fresh $id
                        }
                }
                query {
                        if $in_fresh_ranges then {
                                incr actually_fresh
                        }
                }
        }
}

puts $actually_fresh
puts $potentially_fresh
