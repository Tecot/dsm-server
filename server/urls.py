'''
File name: 
Author: Tecot (tyx_cqbs@163.com)
Version: V1.0
Date: 2024-10-08 11:11:06
Description: 
'''
"""server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from app.views.shared.srp_dir_names_view import SrpDirNamesView
from app.views.shared.get_target_srp_value_view import GetTargetSrpValueView
from app.views.shared.download_sample_data_view import DownloadSampleDataView

from app.views.database.bioproject.geo_data_view import GeoDataView
from app.views.database.bioproject.srp_project_view import SrpProjectView
from app.views.database.bioproject.srp_searched_project_view import SrpSearchedProjectView
from app.views.database.bioproject.run_project_view import RunProjectView
from app.views.database.bioproject.contigs_information_view import ContigsInformationView
from app.views.database.bioproject.contigs_searched_information_view import ContigsSearchedInformationView

from app.views.database.contigproject.contig_project_view import ContigProjectView
from app.views.database.contigproject.contig_project_searched_view import ContigProjectSearchedView

from app.views.database.dataexpress.protein_seq_view import ProteinSeqView
from app.views.database.dataexpress.protein_pdb_view import ProteinPdbView
from app.views.database.dataexpress.cds_vf_resfinder_view import CdsVfResfinderView
from app.views.database.dataexpress.protein_one_seq_view import ProteinOneSeqView
from app.views.database.dataexpress.bin_view import BinView
from app.views.database.dataexpress.macrel_out_prediction_view import MacrelOutPredictionView

from app.views.download.download_view import DownloadView
from app.views.download.download_list_view import DownloadListView

from app.views.analysis.analysis_view import AnalysisView

from app.views.worksapce.task_statuses import TaskStatuses
from app.views.worksapce.download_task_result import DownloadTaskResultView

shared_routes = {
    'srpdirnameview': 'api/shared/srpdirnamesview',
    'gettargetsrpvalue': 'api/shared/gettargetsrpvalue/<str:srp>',
    'downloadsampledata': 'api/shared/downloadsampledata'
}

bioproject_routes = {
    'geodataview': 'api/database/bioproject/geodataview',
    'srpprojectview': 'api/database/bioproject/srpprojectview/<int:current_page>/<int:page_size>',
    'srpsearchedprojectview': 'api/database/bioproject/srpsearchedprojectview',
    'runprojectview': 'api/database/bioproject/runprojectview/<str:srp>',
    'contigsinformationview': 'api/database/bioproject/contigsinformationview/<str:srp>/<int:current_page>/<int:page_size>',
    'contigssearchedinformationview': 'api/database/bioproject/contigssearchedinformationview'
}

contig_project_routes = {
    'contigprojectview': 'api/database/contigproject/contigprojectview/<str:srp>/<int:current_page>/<int:page_size>',
    'contigprojectsearchedview': 'api/database/contigproject/contigprojectsearchedview'
}

data_express_routes = {
    'proteinseqview': 'api/database/dataexpress/proteinseqview/<str:srp>',
    'proteinpdbview': 'api/database/dataexpress/proteinpdbview/<str:srp>/<str:code>',
    'cdsvfresfinderview': 'api/database/dataexpress/cdsvfresfinderView/<str:srp>/<str:contig_ID>',
    'proteinoneseqview': 'api/database/dataexpress/proteinoneseqview/<str:srp>/<str:code>',
    'binView': 'api/database/dataexpress/binview/<str:srp>',
    'macreloutpredictionview': 'api/database/dataexpress/macreloutpredictionview/<str:srp>/<int:current_page>/<int:page_size>'
}

download_routes = {
    'downloadlist': 'api/downloadlist/<int:current_page>/<int:page_size>',
    'download': 'api/download/<str:srp>'
}

analysis_routes = {
    'analysis': 'api/analysis/analysisview'
}

workspace_routes = {
    'taskstatuesview': 'api/workspace/taskstatuesview/<str:keys_str>',
    'downloadtaskresultview': 'api/workspace/downloadtaskresultview/<str:id>'
}

urlpatterns = [
    path('admin/', admin.site.urls),

    path(shared_routes['srpdirnameview'], SrpDirNamesView.as_view()),
    path(shared_routes['gettargetsrpvalue'], GetTargetSrpValueView.as_view()),
    path(shared_routes['downloadsampledata'], DownloadSampleDataView.as_view()),

    path(bioproject_routes['geodataview'], GeoDataView.as_view()),
    path(bioproject_routes['srpprojectview'], SrpProjectView.as_view()),
    path(bioproject_routes['srpsearchedprojectview'], SrpSearchedProjectView.as_view()),
    path(bioproject_routes['runprojectview'], RunProjectView.as_view()),
    path(bioproject_routes['contigsinformationview'], ContigsInformationView.as_view()),
    path(bioproject_routes['contigssearchedinformationview'], ContigsSearchedInformationView.as_view()),

    path(contig_project_routes['contigprojectview'], ContigProjectView.as_view()),
    path(contig_project_routes['contigprojectsearchedview'], ContigProjectSearchedView.as_view()),

    path(data_express_routes['proteinseqview'], ProteinSeqView.as_view()),
    path(data_express_routes['proteinpdbview'], ProteinPdbView.as_view()),
    path(data_express_routes['cdsvfresfinderview'], CdsVfResfinderView.as_view()),
    path(data_express_routes['proteinoneseqview'], ProteinOneSeqView.as_view()),
    path(data_express_routes['binView'], BinView.as_view()),
    path(data_express_routes['macreloutpredictionview'], MacrelOutPredictionView.as_view()),

    path(download_routes['downloadlist'], DownloadListView.as_view()),
    path(download_routes['download'], DownloadView.as_view()),


    
    path(analysis_routes['analysis'], AnalysisView.as_view()),

    path(workspace_routes['taskstatuesview'], TaskStatuses.as_view()),
    path(workspace_routes['downloadtaskresultview'], DownloadTaskResultView.as_view())
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
