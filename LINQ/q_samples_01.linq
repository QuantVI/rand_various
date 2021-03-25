<Query Kind="Statements" />

/*
aggregates-1.md
aggregates-2.md
aggregates-3.md
aggregates-4.md
aggregates.md
conversions.md
Update conversions.md
elements.md
generators.md
groupings-2.md
groupings-3.md
groupings.md
join-operators.md
orderings-2.md
orderings-3.md
orderings-4.md
orderings-5.md
orderings.md
partitions-2.md
partitions.md
projections-2.md
projections-3.md
projections-4.md
projections-5.md
projections.md
quantifiers.md
query-execution.md
restrictions.md
sequence-operations.md
sets-2.md
sets.md
*/

int[] numbers = {5,4,1,3,9,8,6,7,2,0};
var first3numbers = numbers.Take(3);
Console.WriteLine("First 3 numbers:");
foreach (var n in first3numbers)
{
Console.Write(n);
}
