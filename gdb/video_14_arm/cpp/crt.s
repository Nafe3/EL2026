.cpu cortex-m3
.thumb

.section .text._reset
// end of 20K RAM
.word 0x20005000
.word _reset
.thumb_func
.global _reset
_reset:
    bl main
    b .
