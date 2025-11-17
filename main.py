import argparse
import config
from backends import mock



def add_command(title):
    if config.backend == 'mock':
        mock.todo_add(title)


def list_command():
    if config.backend == 'mock':
        mock.todo_list()


def done_command(title):
    if config.backend == 'mock':
        mock.todo_done(title)


def main():
    parser = argparse.ArgumentParser(
        description="A to-do app for scatterbrained individuals."
    )

    subparsers = parser.add_subparsers(dest="command")

    add_parser = subparsers.add_parser("add", help="Add a new idea")
    add_parser.add_argument("title", help="Title of the idea")

    list_parser = subparsers.add_parser("list", help="List current ideas")

    done_parser = subparsers.add_parser("done", help="Mark idea as done")
    done_parser.add_argument("title", help="Title of the idea to mark as done")

    args = parser.parse_args()

    if args.command == "add":
        add_command(args.title)
    elif args.command == "list":
        list_command()
    elif args.command == "done":
        done_command(args.title)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
