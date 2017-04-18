import scipy as sp
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches


def analize_graphs(N, xfile, y1file, y2file, y3file, maxfile = "max_filename.txt", medfile = "medium_filename.txt", minfile = "min_filename.txt", scrfile = "screenshot.png"):
	x = sp.genfromtxt(xfile, delimiter = ', ');
	x = x[:N]
	y1 = sp.genfromtxt(y1file, delimiter = ', ');
	y1 = y1[:N]
	y2 = sp.genfromtxt(y2file, delimiter = ', ');
	y2 = y2[:N]
	y3 = sp.genfromtxt(y3file, delimiter = ', ');
	y3 = y3[:N]

	plt.rcParams["figure.figsize"] = (20,10)
	l = plt.subplot(121) # numrows, numcols, fignum
	
	l.plot(x, y1, c = "red")
	l.plot(x, y2, c = "green")
	l.plot(x, y3, c = "blue")
	y1_patch = mpatches.Patch(color = 'red', label = "y1")
	y2_patch = mpatches.Patch(color = 'green', label = "y2")
	y3_patch = mpatches.Patch(color = 'blue', label = "y3")
	plt.legend(handles=[y1_patch, y2_patch, y3_patch])
	
	plt.xlabel("Abscissa")
	plt.ylabel("Ordinate")
	plt.title("Graph")

	mx = sp.maximum(y1, y2)
	mx = sp.maximum(mx, y3)
	mn = sp.minimum(y1, y2)
	mn = sp.minimum(mn, y3)
	av = sp.average([y1, y2, y3], axis = 0)

	r = plt.subplot(122) 
	r.plot(x, mn, c = "blue")
	r.plot(x, mx, c = "red")
	r.plot(x, av, c = "green")
	y1_patch = mpatches.Patch(color = 'red', label = "Maximum")
	y2_patch = mpatches.Patch(color = 'green', label = "Average")
	y3_patch = mpatches.Patch(color = 'blue', label = "Minimum")
	plt.legend(handles=[y1_patch, y2_patch, y3_patch])
	plt.xlabel("Abscissa")
	plt.ylabel("Ordinate")
	plt.title("Graph")

	sp.savetxt(maxfile, mx, delimiter = ", ")
	sp.savetxt(minfile, mn, delimiter = ", ")
	sp.savetxt(medfile, av, delimiter = ", ")
	plt.savefig(scrfile)
	plt.show()




analize_graphs(500, "x_filename.txt", "y1_filename.txt", "y2_filename.txt", "y3_filename.txt", "max_filename.txt");