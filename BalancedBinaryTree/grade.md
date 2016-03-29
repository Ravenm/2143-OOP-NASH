## Program 2 - Binary Tree Balanced Loading
| #       | Item                                                                         | Value       | Earned   |                |
|:--------|:-----------------------------------------------------------------------------|------------:|---------:|:---------------|
| ***1*** | ***General***                                                                |             |          |                |
| -       | Code was on github                                                           | pass/fail   |          | ![Alt text][1] |
| -       | Code could be ran.                                                           | pass/fail   |          | ![Alt text][1] |
| -       | Code was commented                                                           |    15       |    15    | ![Alt text][1] |
| -       | Followed naming conventions (named your file correctly).                     |             |          |                |
|         |      Classname: BinarySearch to BalancedSearch                               |    5        |     5    | ![Alt text][1] |
|         |     Foldername: BalancedBinaryTree for all your files.                       |    5        |     5    | ![Alt text][1] |   
|         |     Renamed binary_search_tree_list.py to balanced_binary_tree.py            |    5        |     5    | ![Alt text][1] |
| ***2*** | ***Prompted User***                                                          |             |          |                |
| -       | asked user                                                                   |    10       |    10    | ![Alt text][1] |
| -       | used entered value                                                           |    10       |    10    | ![Alt text][1] |
| ***3*** | ***Balanced Tree***                                                          |             |          |                |
| -       | worked                                                                       |    25       |    20    | ![Alt text][3] |
| ***E*** | ***Added Method***                                                           |             |          |                |
| -       | Added insert method that received an entire list                             |    10       |    10    | ![Alt text][1] |
|         | Totals:                                                                      | **100**     |  **95** | ![Alt text][1] |

### Comments:
- Good job!
- Only issue was when I inserted `    intlist = [1, 2, 3, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]`
- It turned into:

```
[-1, 8, 4, 12, 2, 6, 10, 14, 1, 3, 5, 7, 9, 11, 13, 15, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
```

- I didn't want to track it down, but I'm assuming you "extend" or double the size when it's not necessary. 
- Other than that, nice.

[1]: http://f.cl.ly/items/3E231i211n2E042B1U3K/right.png  "Correct"
[2]: http://f.cl.ly/items/2X473C1Q1F2x3S1E4231/wrong.gif  "Incorrect"
[3]: http://f.cl.ly/items/1A0d2Q1J1N1u0C3g0C1s/null.gif  "Errors"
