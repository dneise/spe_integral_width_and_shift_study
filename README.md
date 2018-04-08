# spe_integral_width_and_shift_study

To repeat this study, you need a 10k digicamtoy mont carlo file.
After installing digicamtoy, you gotta adjust `dark.yml` according to you local needs, then execute it like this:

    python produce_data.py -y config_files/dark.yml
    
After you have this file, you can do an spe analysis on it using the `digicampipe-spe` program. 
This program has two parameters we vary in this study `shift` and `integration_window`.

Calling this program multiple times is a nuisance, so there is a little python-script, 
which can create a little bash script for you, which in turn calls `digicampipe-spe` multiple times.

I prepared it, so that it always starts 6 jobs (since I have 8 cores on my laptop and do not want to use all of them) 
and then waits about 5 minutes until the 6 jobs are done, then it does the next 6 jobs and so on.

After all the spe-analysis are done one can look into them and fit some functions to the charge spectra of the extracted pulses.
The result can be seen in the ipython notebook in this folder.

