Attribute VB_Name = "M�dulo1"

sub CalcularComision()
    dim i as integer
    i = 2

    do while cells(i,2)<>""
        cells(i,3)=cells(i,2)*0.10
        i = i + 1
    loop
end sub
