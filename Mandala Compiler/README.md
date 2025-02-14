# User Manual - Mandala Compiler

## Table of Contents
1. Introduction
2. Basic Structure
3. Available Patterns
4. General Attributes
5. Specific Attributes
6. Usage Examples
7. Troubleshooting

## 1. Introduction

The Mandala Compiler is a tool that allows you to create custom mandalas using a simple and specific language. This manual will guide you through the process of creating your own mandalas.

## 2. Basic Structure

Every program must follow this structure:
```
START
[pattern definitions]
END
```

- `START`: Indicates the beginning of the program
- `END`: Indicates the end of the program
- Between `START` and `END`, you define one or more patterns

## 3. Available Patterns

The compiler supports the following patterns:

1. `CIRCLE`: Simple circle
2. `DIAMOND`: Diamond shape
3. `TRIANGLE`: Triangle
4. `SQUARE`: Square
5. `STAR`: Star with variable number of points
6. `LOTUS`: Lotus flower
7. `MAZE`: Maze pattern
8. `PETALS_RADIATE`: Petals radiating from center
9. `DOTS`: Dots in circular arrangement
10. `YINYANG`: Yin Yang symbol

## 4. General Attributes

Each pattern must include these mandatory attributes:

- `SIZE`: Pattern size (positive number)
- `COLOR`: Color in hexadecimal format (example: #FF0000)
- `REPEAT`: Number of pattern repetitions (positive number)

Format:
```
PATTERN [type] SIZE [number] COLOR [#hexcolor] REPEAT [number]
```

## 5. Specific Attributes

Some patterns require additional attributes:

- `STAR`: Requires `POINTS` (number of points, minimum 3)
  ```
  PATTERN STAR SIZE 85 COLOR #FFA500 REPEAT 3 POINTS 5
  ```

- `LOTUS`: Requires `PETALS` (number of petals)
  ```
  PATTERN LOTUS SIZE 95 COLOR #FF1493 REPEAT 2 PETALS 8
  ```

- `MAZE`: Requires `LEVELS` (number of levels)
  ```
  PATTERN MAZE SIZE 75 COLOR #4B0082 REPEAT 2 LEVELS 4
  ```

- `DOTS`: Requires `COUNT` (number of dots)
  ```
  PATTERN DOTS SIZE 85 COLOR #DC143C REPEAT 3 COUNT 16
  ```

## 6. Usage Examples

### Simple Example - Circle
```
START
PATTERN CIRCLE SIZE 100 COLOR #FF0000 REPEAT 3
END
```

### 5-Point Star Example
```
START
PATTERN STAR SIZE 85 COLOR #FFA500 REPEAT 3 POINTS 5
END
```

### Complex Example - Multiple Patterns
```
START
PATTERN CIRCLE SIZE 150 COLOR #4B0082 REPEAT 3
PATTERN STAR SIZE 120 COLOR #FF1493 REPEAT 2 POINTS 7
PATTERN LOTUS SIZE 90 COLOR #00FF00 REPEAT 2 PETALS 6
PATTERN DOTS SIZE 60 COLOR #0000FF REPEAT 3 COUNT 12
END
```

## 7. Troubleshooting

### Error: "Missing SIZE/COLOR/REPEAT attribute"
- Ensure all mandatory attributes are included for each pattern
- Verify they are written in uppercase

### Error: "Invalid color"
- Colors must be in hexadecimal format
- Must start with # and have 6 hexadecimal characters
- Correct example: #FF0000
- Incorrect example: FF0000

### Error: "Invalid numeric value"
- All numeric values (SIZE, REPEAT, POINTS, etc.) must be positive
- Negative numbers or zero are not allowed

### Error: "Pattern not recognized"
- Verify the pattern name is spelled correctly and in uppercase
- Check the list of available patterns

### Error: "Missing specific attribute"
- STAR needs POINTS
- LOTUS needs PETALS
- MAZE needs LEVELS
- DOTS needs COUNT

### Error: "Tokens found after END"
- Make sure there is no code after the END keyword
- All code must be between START and END

---

**Note**: For best results:
- Maintain a consistent order in attributes
- Use reasonable values for SIZE (50-150 recommended)
- Experiment with different pattern combinations
- Try different REPEAT values to create interesting effects

## Color Reference Guide

Common colors in hexadecimal format:
- Red: #FF0000
- Green: #00FF00
- Blue: #0000FF
- Yellow: #FFFF00
- Purple: #800080
- Orange: #FFA500
- Pink: #FF1493
- Black: #000000
- White: #FFFFFF

## Pattern Attributes Quick Reference

| Pattern | Required Attributes | 
|---------|---------------------|
| CIRCLE  | SIZE, COLOR, REPEAT | 
| DIAMOND | SIZE, COLOR, REPEAT | 
| TRIANGLE| SIZE, COLOR, REPEAT | 
| SQUARE  | SIZE, COLOR, REPEAT | 
| STAR    | SIZE, COLOR, REPEAT, POINTS |
| LOTUS   | SIZE, COLOR, REPEAT, PETALS |
| MAZE    | SIZE, COLOR, REPEAT, LEVELS |
| DOTS    | SIZE, COLOR, REPEAT, COUNT |
| YINYANG | SIZE, COLOR, REPEAT |
