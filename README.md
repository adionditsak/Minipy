Minipy
======

Minify and concatenate js + css files with automatic detection.

As module you can eg. use it like this:
        import minipy.mini

        mini = minipy.mini.Minify()
        concat = mini.mini.Concat()

        # to minify
        mini.run(['file1.js', 'file2.js'])

        # to concat
        concat.run(['file1.js', 'file2.js'])

As CLI use like:
        # to minify
        python mini.py -m file1.js file2.js ...

More to come
