import boto3


# create a dictionary with names of databases or instances as key and their volume ids as value
volumes_dict = {
                  'siddharth' : 'vol-0c94b9972d85052e7',
                
          }
# create a dictionary of snapshots with their snapshot ids which were created successfully
successful_snapshots = dict()
# iterate through each item in volumes_dict and use key as description of snapshot
for snapshot in volumes_dict:
    try:
        response = client.create_snapshot(
            Description= snapshot,
            VolumeId= volumes_dict[snapshot],
            DryRun= False
        )
        # response is a dictionary containing ResponseMetadata and SnapshotId
        status_code = response['ResponseMetadata']['HTTPStatusCode']
        snapshot_id = response['SnapshotId']
        # check if status_code was 200 or not to ensure the snapshot was created successfully
        if status_code == 200:
            successful_snapshots[snapshot] = snapshot_id
    except Exception as e:
        exception_message = "There was error in creating snapshot " + snapshot + " with volume id "+volumes_dict[snapshot]+" and error is: \n"\
                            + str(e)
# print the snapshots which were created successfully
print(successful_snapshots)
