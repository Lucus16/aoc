set handle [open day1.in r]
set input [read $handle]
close $handle

set position 50
set zero_end_count 0
set zero_click_count 0
lmap rotation $input {
        set direction [string index $rotation 0]
        set amount [string range $rotation 1 end]
        if {$direction == "R"} then {
                incr zero_click_count [expr {($position + $amount) / 100 - $position / 100}]
                set position [expr {$position + $amount}]
        } else {
                incr zero_click_count [expr {($position - 1) / 100 - ($position - $amount - 1) / 100}]
                set position [expr {$position - $amount}]
        }
        if {$position % 100 == 0} then {
                incr zero_end_count
        }
}
puts $zero_end_count
puts $zero_click_count
