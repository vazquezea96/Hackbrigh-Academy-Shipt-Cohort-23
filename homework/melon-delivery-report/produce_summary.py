def produce_summary_report(day, the_file_day):
    print(day)
    the_file = open(the_file_day)
    for line in the_file:
        line = line.rstrip()
        words = line.split('|')

       
    melon = words[0]
    count = words[1]
    amount = words[2]
    print(f"Delivered {count} {melon}s for total of ${amount}")
    the_file.close()

produce_summary_report("Day 1", "um-deliveries-day-1.txt")
produce_summary_report("Day 2", "um-deliveries-day-2.txt")
produce_summary_report("Day 3", "um-deliveries-day-3.txt")
