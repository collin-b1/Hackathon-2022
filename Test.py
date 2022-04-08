from LunchLine import LunchLine


def main():
    lunch_line = LunchLine()

    while True:
        print('would you like to add or remove a student? (a/r)')
        i = input()

        if i == 'a':
            lunch_line.add_student()

        if i == 'r':
            lunch_line.remove_student()

        if i == 's':
            lunch_line.save_daily_data()

        print()
        print('current line length:', len(lunch_line.students))
        print('current times:', lunch_line.times)
        if len(lunch_line.times) > 0:
            print('estimated wait time:', lunch_line.get_estimate(), 's')
            print('current avg wait time:', lunch_line.get_avg(len(lunch_line.times)), 's')
        print()


if __name__ == "__main__":
    main()
