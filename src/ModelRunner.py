from src.Visualizer import Visualizer


class ModelRunner(object):
    def run(self, plane_model, rows=3, seats=3, visualize=False):
        plane = plane_model.generate(rows, seats)

        if (visualize):
            visualizer = Visualizer(plane)
            visualizer.run()
        else:
            for plane_step, time in plane.step():
                print("Time Unit: ", time)
                print(plane_step)
