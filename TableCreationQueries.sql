
create database threedprint character set utf8mb4;

use threedprint;

-- Users table
CREATE TABLE `Users` (
  `Id` INT NOT NULL,
  `Reputation` INT NULL,
  `CreationDate` DATETIME NULL,
  `DisplayName` VARCHAR(512) NULL,
  `LastAccessDate` DATETIME NULL,
  `Location` TEXT NULL,
  `AboutMe` MEDIUMTEXT NULL,
  `Views` INT NULL,
  `UpVotes` INT NULL,
  `DownVotes` INT NULL,
  `Age` INT NULL,
  `AccountId` INT NULL,
  `ProfileImageUrl` TEXT NULL,
  `WebsiteUrl` TEXT NULL,
  PRIMARY KEY (`Id`)
);

-- Posts table
CREATE TABLE `Posts` (
  `Id` INT NOT NULL,
  `PostTypeId`  INT NULL,
  `AcceptedAnswerId`  INT NULL,
  `CreationDate`  DATETIME NULL,
  `Score` INT NULL,
  `ViewCount` INT NULL,
  `Body`  MEDIUMTEXT NULL,
  `OwnerUserId` INT NULL,
  `LastActivityDate`  DATETIME  NULL,
  `Title` TEXT NULL,
  `Tags`  TEXT NULL,
  `AnswerCount` INT NULL,
  `CommentCount`  INT NULL,
  `LastEditorUserId`  INT NULL,
  `LastEditDate`  DATETIME NULL,
  `FavoriteCount` INT NULL,
  `ParentId`  INT NULL,
  `ClosedDate`  DATETIME NULL,
  `OwnerDisplayName`  VARCHAR(512) NULL,
  `LastEditorDisplayName` VARCHAR(512) NULL,
  `CommunityOwnedDate` DATETIME NULL,
  PRIMARY KEY (`Id`)
);

-- Tags table
CREATE TABLE `Tags` (
  `Id` INT NOT NULL,
  `TagName` TEXT NULL,
  `Count` INT NULL,
  `ExcerptPostId` INT NULL,
  `WikiPostId`  INT NULL,
  PRIMARY KEY (`Id`)
  );

-- Votes table
CREATE TABLE `Votes` (
  `Id` INT NOT NULL,
  `PostId`  INT NULL,
  `VoteTypeId`  INT NULL,
  `CreationDate`  DATETIME NULL,
  `UserId`  INT NULL,
  `BountyAmount`  INT NULL,
  PRIMARY KEY (`Id`)
);

-- PostLinks table
CREATE TABLE `PostLinks` (
  `Id` INT NOT NULL,
  `CreationDate`  DATETIME NULL,
  `PostId`  INT NULL,
  `RelatedPostId` INT NULL,
  `LinkTypeId`  INT NULL,
  PRIMARY KEY (`Id`)
);

-- PostHistory table
CREATE TABLE `PostHistory` (
  `Id` INT NOT NULL,
  `PostHistoryTypeId` INT NULL,
  `PostId`  INT NULL,
  `RevisionGUID`  TEXT NULL,
  `CreationDate`  DATETIME NULL,
  `UserId`  INT NULL,
  `Text`  MEDIUMTEXT NULL,
  `Comment` MEDIUMTEXT NULL,
  `UserDisplayName` VARCHAR(512) NULL,
  PRIMARY KEY (`Id`)
);

-- Comments table
CREATE TABLE `Comments` (
  `Id` INT NOT NULL,
  `PostId`  INT NULL,
  `Score` INT NULL,
  `Text`  MEDIUMTEXT NULL,
  `CreationDate`  DATETIME NULL,
  `UserId`  INT NULL,
  `UserDisplayName` VARCHAR(512) NULL,
  PRIMARY KEY (`Id`)
);


-- Badges table
CREATE TABLE `Badges` (
  `Id` INT NOT NULL,
  `UserId`  INT NULL,
  `Name`  VARCHAR(512) NULL,
  `Date`  DATETIME NULL,
  `Class` INT NULL,
  `TagBased`  VARCHAR(40) NULL,
  PRIMARY KEY (`Id`)
);