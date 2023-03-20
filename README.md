# Can Laptop interface

## Can Monitor

### Communication on the serial:
1, First send a "monitor" string encoded in utf-8 on serial
2, It catches all packet on the CAN bus and sends transfers it to the serial
    Format:
    
    