proc sum xs {
        set result 0
        foreach x $xs {
                incr result $x
        }
        return $result
}

proc min xs {
        set result ""
        foreach x $xs {
                if {[string length $result] == 0 || $x < $result} {
                        set result $x
                }
        }
        return $result
}

proc max xs {
        set result ""
        foreach x $xs {
                if {[string length $result] == 0 || $x > $result} {
                        set result $x
                }
        }
        return $result
}
