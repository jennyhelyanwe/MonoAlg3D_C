import matplotlib
matplotlib.use('tkagg')
import matplotlib.pyplot as pyplot
import numpy as np
from matplotlib.gridspec import GridSpec
import matplotlib.animation as animation

fig = pyplot.figure(tight_layout=True, figsize=[12,7])
fig.suptitle('DTI032')

gs = GridSpec(3,4)
ax5 = fig.add_subplot(gs[0,0])
ax6 = fig.add_subplot(gs[1,0])
ax7 = fig.add_subplot(gs[2,0])
ax8 = fig.add_subplot(gs[0,1])
ax9 = fig.add_subplot(gs[1,1])
ax10 = fig.add_subplot(gs[2,1])
ax11 = fig.add_subplot(gs[0,2])
ax12 = fig.add_subplot(gs[1,2])
ax13 = fig.add_subplot(gs[2,2])
ax14 = fig.add_subplot(gs[0,3])
ax15 = fig.add_subplot(gs[1,3])
ax16 = fig.add_subplot(gs[2,3])

clinical_ecg = np.loadtxt('/mnt/scratch/jenny/DTI032_clinical_full_ecg.csv', delimiter=',')
max_leads = np.amax(clinical_ecg)
clinical_I = clinical_ecg[0,:]/max_leads
clinical_II = clinical_ecg[1,:]/max_leads
clinical_V1 = clinical_ecg[2,:]/max_leads
clinical_V2 = clinical_ecg[3,:]/max_leads
clinical_V3 = clinical_ecg[4,:]/max_leads
clinical_V4 = clinical_ecg[5,:]/max_leads
clinical_V5 = clinical_ecg[6,:]/max_leads
clinical_V6 = clinical_ecg[7,:]/max_leads
clinical_t = np.arange(0, len(clinical_I), 1)
ax5.plot(clinical_t, clinical_I, 'k')
ax6.plot(clinical_t, clinical_II, 'k')
ax7.plot(clinical_t, clinical_V1, 'k')
ax8.plot(clinical_t, clinical_V2, 'k')
ax9.plot(clinical_t, clinical_V3, 'k')
ax10.plot(clinical_t, clinical_V4, 'k')
ax11.plot(clinical_t, clinical_V5, 'k')
ax12.plot(clinical_t, clinical_V6, 'k')
monoalg_activation_offset = 37.46 # [ms]
def animate(i):
	filename = 'ecg.txt'
	#with open(filename,'r') as f:
	#		data = f.readlines()
	data = np.genfromtxt('ecg.txt', skip_footer=1)
	t = data[:, 0] - monoalg_activation_offset
	LA = data[:, 1]
	RA = data[:, 2]
	LL = data[:, 3]
	RL = data[:, 4]
	V1 = data[:, 5]
	V2 = data[:, 6]
	V3 = data[:, 7]
	V4 = data[:, 8]
	V5 = data[:, 9]
	V6 = data[:, 10]

	# Ealuate Wilson's central terminal
	VW = 1.0/3.0*(RA + LA + LL)

	# Evaluate simulated ECG lead traces
	V1 = V1 - VW
	V2 = V2 - VW
	V3 = V3 - VW
	V4 = V4 - VW
	V5 = V5 - VW
	V6 = V6 - VW
	I = LA - RA
	II = LL - RA
	III = LL - LA
	aVL = LA - (RA + LL)/2.0
	aVF = LL - (LA + RA)/2.0
	aVR = RA - (LA + LL)/2.0
	all_leads = np.concatenate((V1,V2,V3,V4,V5,V6,I,II,III,aVR,aVL,aVF))
	max_all_leads = max(abs(all_leads))

	ax5.clear()
	ax5.plot(t, I/max_all_leads, 'b', clinical_t, clinical_I, 'k')
	ax6.clear()
	ax6.plot(t, II/max_all_leads, 'b', clinical_t, clinical_II, 'k')
	ax7.clear()
	ax7.plot(t, III/max_all_leads, 'b')
	ax8.clear()
	ax8.plot(t, aVR/max_all_leads, 'b')
	ax9.clear()
	ax9.plot(t, aVL/max_all_leads, 'b')
	ax10.clear()
	ax10.plot(t, aVF/max_all_leads, 'b')

	ax11.clear()
	ax11.plot(t, V1/max_all_leads,'b', clinical_t, clinical_V1, 'k')
	ax12.clear()
	ax12.plot(t, V2/max_all_leads, 'b', clinical_t, clinical_V2, 'k')
	ax13.clear()
	ax13.plot(t, V3/max_all_leads,'b',  clinical_t, clinical_V3, 'k')
	ax14.clear()
	ax14.plot(t, V4/max_all_leads,'b', clinical_t, clinical_V4, 'k')
	ax15.clear()
	ax15.plot(t, V5/max_all_leads,'b', clinical_t, clinical_V5, 'k')
	ax16.clear()
	ax16.plot(t, V6/max_all_leads,'b', clinical_t, clinical_V6, 'k')

	ax5.set_xlabel('Time (s)')
	ax6.set_xlabel('Time (s)')
	ax7.set_xlabel('Time (s)')
	ax8.set_xlabel('Time (s)')
	ax9.set_xlabel('Time (s)')
	ax10.set_xlabel('Time (s)')
	ax11.set_xlabel('Time (s)')
	ax12.set_xlabel('Time (s)')
	ax13.set_xlabel('Time (s)')
	ax14.set_xlabel('Time (s)')
	ax15.set_xlabel('Time (s)')
	ax16.set_xlabel('Time (s)')

	ax5.set_ylabel('Normalised ECG')
	ax6.set_ylabel('Normalised ECG')
	ax7.set_ylabel('Normalised ECG')
	ax8.set_ylabel('Normalised ECG')
	ax9.set_ylabel('Normalised ECG')
	ax10.set_ylabel('Normalised ECG')
	ax11.set_ylabel('Normalised ECG')
	ax12.set_ylabel('Normalised ECG')
	ax13.set_ylabel('Normalised ECG')
	ax14.set_ylabel('Normalised ECG')
	ax15.set_ylabel('Normalised ECG')
	ax16.set_ylabel('Normalised ECG')

	ax5.set_ylim(-1,1)
	ax6.set_ylim(-1,1)
	ax7.set_ylim(-1,1)
	ax8.set_ylim(-1,1)
	ax9.set_ylim(-1,1)
	ax10.set_ylim(-1,1)
	ax11.set_ylim(-1,1)
	ax12.set_ylim(-1,1)
	ax13.set_ylim(-1,1)
	ax14.set_ylim(-1,1)
	ax15.set_ylim(-1,1)
	ax16.set_ylim(-1,1)

	ax5.set_title('I')
	ax6.set_title('II')
	ax7.set_title('III')
	ax8.set_title('aVR')
	ax9.set_title('aVL')
	ax10.set_title('aVF')
	ax11.set_title('V1')
	ax12.set_title('V2')
	ax13.set_title('V3')
	ax14.set_title('V4')
	ax15.set_title('V5')
	ax16.set_title('V6')


ani = animation.FuncAnimation(fig, animate, interval=1000)
pyplot.show(block=True)

