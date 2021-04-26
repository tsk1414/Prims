# Prims

A blizzard has made a lot of roads in the county impassable so citizens are cut off from
essential resources. The county’s snow plows are working overtime to get everyone recononected to the road network. You are given the towns and roads in the county, as well as the
amount of time it will take to plow the roads. You must find the minimum amount of time
it will take to get everyone reconnected.

Input

• The first line will contain an integer n, the number of towns that are stranded.

• The next n lines will contain those towns.

• The next line will contain an integer r, the number of roads in need of plowing.

• The next r lines will contain the roads in the format of comma-separated endpoints,
followed by an integer, the amount of time required to plow it.

All towns must be reachable after plowing the roads. Any town that is disconnected is a
valid connection point.

Output

A single line containing an integer, the amount of time it will take to get everyone recononected.

Sample Input

7

Newark

Montclair

Livingston

Caldwell

Fairfield

Belleville

Roseland

9

Newark , Livingston , 80

Newark , Roseland , 10

Newark , Belleville , 20

Livingston , Fairfield , 15

Livingston , Montclair , 30

Fairfield , Montclair , 45

Caldwell , Belleville , 25

Caldwell , Fairfield , 15

Belleville , Fairfield , 10
