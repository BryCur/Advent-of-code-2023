tile_count = 0
enclosingPipes = pipes_connecting_north.union(pipes_connecting_south)
met_enclosing_pipe = False
for i, line in enumerate(pipe_map_copy):
    met_enclosing_pipe = False
    line_count = 0
    for j, char in enumerate(line): 
        if (i, j) in loopPath and char in enclosingPipes:
            if met_enclosing_pipe: 
                tile_count += line_count
                line_count = 0
            else:
                met_enclosing_pipe = True
        elif met_enclosing_pipe and (i, j) not in loopPath:
            line_count += 1