set handle [open day3.in r]
set input [read $handle]
close $handle

source math.tcl

foreach battery_count [list 2 12] {
        puts [sum [lmap bank $input {
                string cat {*}[lmap i [range $battery_count-1 -1 -1] {
                        set digit [max [split [string byterange $bank 0 end-$i] ""]]
                        set pos [string first $digit $bank]
                        set bank [string byterange $bank $pos+1 end]
                        list $digit
                }]
        }]]
}
