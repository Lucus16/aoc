set handle [open day4.in r]
set input [read $handle]
close $handle

proc count {y xs} {
        set result 0
        foreach x $xs {
                if [string equal $x $y] then {
                        incr result
                }
        }
        return $result
}

proc togrid lines {lmap line $lines {split $line ""}}
proc showgrid grid {foreach row $grid {puts $row}}
proc gridwidth grid {llength [lindex $grid 0]}
proc gridheight grid {llength $grid}
proc gridget {grid x y} {lindex [lindex $grid $y] $x}
proc gridmap {grid xVar yVar cVar body} {
        lmap $yVar [range [llength $grid]] row $grid {
                lmap $xVar [range [llength $row]] $cVar $row $body
        }
}

set grid [togrid $input]

proc step grid {
        gridmap $grid x y c {
                set adjacent_rolls [count @ [lmap dx {-1 -1 -1 0 0 1 1 1} dy {-1 0 1 -1 1 -1 0 1} {
                        gridget $grid $x+$dx $y+$dy
                }]]
                if {$c eq "@" && $adjacent_rolls < 4} then {
                        list x
                } else {
                        list $c
                }
        }
}

set grid [step $grid]
set num_removed [count x [concat {*}$grid]]
puts $num_removed
while 1 {
        set new_grid [step $grid]
        set new_num_removed [count x [concat {*}$new_grid]]
        if {$new_num_removed == $num_removed} break
        set grid $new_grid
        set num_removed $new_num_removed
}
puts $num_removed
